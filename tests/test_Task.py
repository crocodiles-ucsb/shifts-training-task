import src.Task as task


def test_app():
    input_values = ["3 10", "10 45 50"]
    output = []

    def mock_input():
        return input_values.pop(0)

    task.input = mock_input
    task.print = lambda s: output.append(s)

    task.task()

    assert output == [0]
