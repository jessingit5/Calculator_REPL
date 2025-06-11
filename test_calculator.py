

import pytest
from unittest.mock import MagicMock

from calculator import add, subtract, multiply, divide, get_number, get_operation, run_calculator_repl, main



@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 8),
    (-1, 1, 0),
    (-5, -5, -10),
    (2.5, 1.5, 4.0)
])
def test_add(a, b, expected):

    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 3, 7),
    (2, 5, -3),
    (-5, -5, 0),
    (5.5, 1.5, 4.0)
])
def test_subtract(a, b, expected):

    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 4, 8),
    (-3, 5, -15),
    (-2, -3, 6),
    (0, 100, 0)
])
def test_multiply(a, b, expected):

    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (-10, 2, -5),
    (0, 5, 0)
])
def test_divide(a, b, expected):

    assert divide(a, b) == expected

def test_divide_by_zero():

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)



def test_get_number_valid():

    mock_input = MagicMock(return_value="12.5")
    assert get_number("Prompt: ", mock_input) == 12.5

def test_get_number_invalid_then_valid():

    mock_input = MagicMock(side_effect=["abc", "10"])
    assert get_number("Prompt: ", mock_input) == 10

def test_get_operation_valid():

    mock_input = MagicMock(return_value="+")
    assert get_operation(mock_input) == "+"

def test_get_operation_invalid_then_valid():

    mock_input = MagicMock(side_effect=["x", "*"])
    assert get_operation(mock_input) == "*"

def test_run_calculator_repl_single_calculation_and_exit():

    inputs = ["5", "+", "3", "n"]
    mock_input = MagicMock(side_effect=inputs)
    mock_output = MagicMock()

    run_calculator_repl(mock_input, mock_output)

    mock_output.assert_any_call("Result: 5.0 + 3.0 = 8.0")
    mock_output.assert_any_call("Exiting calculator. Goodbye!")

def test_run_calculator_repl_division_by_zero_error():

    inputs = ["10", "/", "0", "n"]
    mock_input = MagicMock(side_effect=inputs)
    mock_output = MagicMock()

    run_calculator_repl(mock_input, mock_output)

    mock_output.assert_any_call("Error: Cannot divide by zero.")

def test_run_calculator_repl_invalid_number_and_continue():

    inputs = ["abc", "10", "-", "2", "y", "100", "*", "2", "n"]
    mock_input = MagicMock(side_effect=inputs)
    mock_output = MagicMock()

    run_calculator_repl(mock_input, mock_output)

    mock_output.assert_any_call("Invalid input. Please enter a valid number.")
    mock_output.assert_any_call("Result: 10.0 - 2.0 = 8.0")
    mock_output.assert_any_call("Result: 100.0 * 2.0 = 200.0")

def test_run_calculator_repl_invalid_operation():

    inputs = ["10", "x", "*", "5", "n"]
    mock_input = MagicMock(side_effect=inputs)
    mock_output = MagicMock()

    run_calculator_repl(mock_input, mock_output)

    mock_output.assert_any_call("Invalid operation 'x'. Please try again.")
    mock_output.assert_any_call("Result: 10.0 * 5.0 = 50.0")

def test_run_calculator_repl_invalid_continue_choice():

    inputs = ["1", "+", "1", "maybe", "n"]
    mock_input = MagicMock(side_effect=inputs)
    mock_output = MagicMock()

    run_calculator_repl(mock_input, mock_output)

    mock_output.assert_any_call("Invalid choice. Please enter 'y' or 'n'.")

def test_run_calculator_repl_keyboard_interrupt():

    mock_input = MagicMock(side_effect=KeyboardInterrupt)
    mock_output = MagicMock()

    run_calculator_repl(mock_input, mock_output)
    mock_output.assert_any_call("\nExiting calculator. Goodbye!")

def test_main(monkeypatch):
    mock_repl = MagicMock()
    
    monkeypatch.setattr("calculator.run_calculator_repl", mock_repl)
    
    main()
    
    mock_repl.assert_called_once()
