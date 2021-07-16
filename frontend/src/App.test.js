import { render, screen } from '@testing-library/react';
import App from './App';

test('renders title', () => {
  render(<App />);
  const linkElement = screen.getByText(/Temperature Converter/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders inputs with default value', () => {
  const result = render(<App />);

  const temperatureInput = result.container.querySelector('#temperatureInput');
  expect(temperatureInput).toHaveValue(0);

  const sourceUnit = screen.getByText(/Source temperature Unit: C/i);
  expect(sourceUnit).toBeInTheDocument();

  const destinationUnit = screen.getByText(/Unit for conversion: F/i);
  expect(destinationUnit).toBeInTheDocument();
});
