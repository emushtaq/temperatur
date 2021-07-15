import * as React from "react";
import Dropdown from 'react-bootstrap/Dropdown';
import {useState} from "react";
import {get} from "axios";

function ConversionForm(props) {

    const unitMap = {'C': 'Centigrade', 'F': 'Fahrenheit', 'K': 'Kelvin'}
    const units = ['C', 'F', 'K']
    const [value, setValue] = useState("0");
    const [source, setSource] = useState(units[0]);
    const [destination, setDestination] = useState(units[1]);
    const [result, setResult] = useState(null);

    const handleChange = (event) => {
        setValue(event.target.value);
        setResult(null);
    }

    const handleSourceChange = (eventKey) => {
        if(eventKey !== source) {
            setSource(eventKey);
            if (destination === eventKey) {
                setDestination(units.filter(unit => unit !== eventKey)[0])
            }
            setResult(null);
        }
    }

    const handleDestinationChange = (eventKey) => {
        setDestination(eventKey);
        setResult(null);
    }

    const handleSubmit = (event) => {
        calculateConversion();
        event.preventDefault();
    }

    const calculateConversion = () => {
        if (source != null && destination != null && value !== "") {
            get('http://localhost:8000/convert?source=' + source + '&destination=' + destination + '&value=' + value)
                .then(response => setResult(response.data + 'º ' + destination));
        } else {
            setResult("Check the inputs");
        }
    }

    return (
        <div class="box">
            <div>
                <h1>
                    Temperature Converter
                </h1>
            </div>
            <div>
                <form onSubmit={handleSubmit}>
                    <div className={'element'}>
                        <label>
                            Enter the temperature:
                            <input className={'temperatureInput'} type="number" value={value} onChange={handleChange}/> º
                        </label>
                    </div>
                    <div className={'element'}>
                        <label>
                            Source temperature Unit: {source}
                            <Dropdown onSelect={handleSourceChange} value={source}>
                                <Dropdown.Toggle variant="success" id="dropdown-source">
                                    Click to toggle unit
                                </Dropdown.Toggle>
                                <Dropdown.Menu>
                                    {units.map(unit => (
                                        <Dropdown.Item eventKey={unit}>{unitMap[unit]}</Dropdown.Item>
                                    ))}
                                </Dropdown.Menu>
                            </Dropdown>
                        </label>
                    </div>
                    <div className={'element'}>
                        <label>
                            Unit for conversion: {destination}
                            <Dropdown onSelect={handleDestinationChange} value={destination}>
                                <Dropdown.Toggle variant="success" id="dropdown-destination">
                                    Click to toggle unit
                                </Dropdown.Toggle>
                                <Dropdown.Menu>
                                    {units.filter(unit => unit!==source).map(unit => (
                                        <Dropdown.Item eventKey={unit}>{unitMap[unit]}</Dropdown.Item>
                                    ))}
                                </Dropdown.Menu>
                            </Dropdown>
                        </label>
                    </div>
                    <div className={'element'}>
                        <input type="submit" value="CONVERT!"/>
                    </div>
                    {result !== null &&
                    <div className={'element'}>
                        <label>
                            Result: {value}º {unitMap[source]} in {unitMap[destination]} is {result}
                        </label>
                    </div>
                    }
                </form>
            </div>
        </div>
    );
}

export default ConversionForm;