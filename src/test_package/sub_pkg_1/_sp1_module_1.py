def m1_fn1(x: str = "default_string") -> str:
    """
    Funktion 1 of module 1 in sub package 1
    
    Args:
        x (str): input string
    
    Returns:
        str : input string with prefix sp1 m1 fn1
    
    Example:
        >>> tp.sp1.m1_fn1("test")
        "sp1 m1 fn1 test"
        
    """

    return f"sp1 m1 fn1 {x}"