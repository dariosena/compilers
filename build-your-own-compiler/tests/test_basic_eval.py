from compiler.main import pl_eval, pl_parse


def test_eval():
    def perform(expression):
        return pl_eval(pl_parse(expression))

    assert perform("1") == 1
    assert perform("(+ 1 2)") == 3
    assert perform("(+ 2 2)") == 4
    assert perform('(? (lt 1 32) "yes" "no")') == "yes"
    assert perform("(print 1 2 3)") is None
