import difflib

def get_differences(text1, text2):
    diff = difflib.HtmlDiff().make_table(
        text1.splitlines(), text2.splitlines(),
        context=True, numlines=2
    )
    return diff
