from typer.testing import CliRunner
import cards


def run_cards(*params):
    runner = CliRunner()
    result = runner.invoke(cards.app, params)
    return result.output.rstrip()


def test_patch_get_path(monkeypatch, tmp_path):
    def fake_get_path():
        return tmp_path

    monkeypatch.setattr(cards.cli,
                        "get_path",
                        fake_get_path)
    assert run_cards("config") == str(tmp_path)
    assert run_cards("count") == "0"