from app import load_report


def test_load_report(tmp_path):
    report = tmp_path / "sample.txt"
    report.write_text(
        "AI assists software engineering.",
        encoding="utf-8"
    )

    text = load_report(report)

    assert text == "AI assists software engineering."

def test_load_report_empty_file(tmp_path):
    report = tmp_path / "empty.txt"
    report.write_text("", encoding="utf-8")
    text = load_report(report)
    assert text == ""

def test_load_report_missing_file(tmp_path):
    report = tmp_path / "missing.txt"
    with pytest.raises(FileNotFoundError):
        load_report(report)