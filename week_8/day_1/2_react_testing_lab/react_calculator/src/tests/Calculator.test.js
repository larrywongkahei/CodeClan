import React from 'react';
import Calculator from '../containers/Calculator';
import {render, fireEvent} from '@testing-library/react';

describe('Calculator', () => {
  let container;
  beforeEach(() => {
    container = render(<Calculator/>)
  })

  it('should change running total on number enter', () => {
    const button4 = container.getByTestId('number4');
    const runningTotal = container.getByTestId('running-total');
    fireEvent.click(button4);
    expect(runningTotal.textContent).toEqual('4');
  })

  it('should add 1 to 4 shows 5', () =>{
    const button1 = container.getByTestId('number1');
    fireEvent.click(button1)
    const addbutton = container.getByTestId('operator-add');
    fireEvent.click(addbutton)
    const button4 = container.getByTestId('number4');
    fireEvent.click(button4);
    const equalButton = container.getByTestId('operator-equals');
    fireEvent.click(equalButton);
    const runningTotal = container.getByTestId('running-total');
    expect(runningTotal.textContent).toEqual('5');
  })

  it('should subtract 4 from 7 and get 3', () =>{
    const button7 = container.getByTestId('number7');
    fireEvent.click(button7);
    const subtractButton = container.getByTestId('operator-subtract');
    fireEvent.click(subtractButton);
    const button4 = container.getByTestId('number4');
    fireEvent.click(button4);
    const equalButton = container.getByTestId('operator-equals');
    fireEvent.click(equalButton);
    const runningTotal = container.getByTestId('running-total');
    expect(runningTotal.textContent).toEqual('3')
  })

  it('should multiply 3 by 5 and get 15', () =>{
    const button3 = container.getByTestId('number3');
    fireEvent.click(button3);
    const multiplyButton = container.getByTestId('operator-multiply');
    fireEvent.click(multiplyButton);
    const button5 = container.getByTestId('number5');
    fireEvent.click(button5);
    const equalButton = container.getByTestId('operator-equals');
    fireEvent.click(equalButton);
    const runningTotal = container.getByTestId('running-total');
    expect(runningTotal.textContent).toEqual('15')
  })

  it('should divide 21 by 7 and get 3', () =>{
    const button2 = container.getByTestId('number2');
    fireEvent.click(button2);
    const button1 = container.getByTestId('number1');
    fireEvent.click(button1);
    const divideButton = container.getByTestId('operator-divide');
    fireEvent.click(divideButton);
    const button7 = container.getByTestId('number7');
    fireEvent.click(button7);
    const equalButton = container.getByTestId('operator-equals');
    fireEvent.click(equalButton);
    const runningTotal = container.getByTestId('running-total');
    expect(runningTotal.textContent).toEqual('3')
  })

  it('should concatenate multiple number button clicks', () =>{
    const button2 = container.getByTestId('number2');
    fireEvent.click(button2);
    fireEvent.click(button2);
    fireEvent.click(button2);
    fireEvent.click(button2);
    const runningTotal = container.getByTestId('running-total');
    expect(runningTotal.textContent).toEqual('2222')
  })

  it('should chain multiple operations together', () =>{
    const button8 = container.getByTestId('number8');
    fireEvent.click(button8);
    const divideButton = container.getByTestId('operator-divide');
    fireEvent.click(divideButton);
    const button2 = container.getByTestId('number2');
    fireEvent.click(button2);
    const addButton = container.getByTestId('operator-add');
    fireEvent.click(addButton);
    const button3 = container.getByTestId('number3');
    fireEvent.click(button3);
    const equalButton = container.getByTestId('operator-equals');
    fireEvent.click(equalButton);
    const runningTotal = container.getByTestId('running-total');
    expect(runningTotal.textContent).toEqual('7')
  })

  it('should clear the running total without affecting the calculation', () =>{
    const button8 = container.getByTestId('number8');
    fireEvent.click(button8);
    const divideButton = container.getByTestId('operator-divide');
    fireEvent.click(divideButton);
    const button2 = container.getByTestId('number2');
    fireEvent.click(button2);
    const equalButton = container.getByTestId('operator-equals');
    fireEvent.click(equalButton);
    const clearButton = container.getByTestId('clear');
    fireEvent.click(clearButton);
    const addButton = container.getByTestId('operator-add');
    fireEvent.click(addButton);
    const button3 = container.getByTestId('number3');
    fireEvent.click(button3);
    fireEvent.click(equalButton);
    const runningTotal = container.getByTestId('running-total');
    expect(runningTotal.textContent).toEqual('7')



  })
})

