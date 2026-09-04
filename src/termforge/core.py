def wrap(text: str, width: int) -> list[str]:
    """Wrap terminal text without splitting words when possible."""
    if width < 1: raise ValueError('width must be positive')
    words=text.split(); lines=[]; current=''
    for word in words:
        if not current: current=word
        elif len(current)+1+len(word)<=width: current+=' '+word
        else: lines.append(current); current=word
    if current: lines.append(current)
    return lines
