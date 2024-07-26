def m1_fn1(x: str = "default_string") -> str:
    """
    Function 1 of module 1 in sub package 1
    
    Args:
        x (str): input string
    
    Returns:
        str : input string with prefix sp1 m1 fn1
    
    Example:
        >>> tp.sp1.m1_fn1("test")
        "sp1 m1 fn1 test"
        
    """

    return f"sp1 m1 fn1 {x}"


def m1_fn2(x: str = "default_string") -> str:
    """
    Function 2 of module 1 in sub package 1
    
    Args:
        x (str): input string
    
    Returns:
        str : input string with prefix sp1 m1 fn1
    
    Example:
        >>> tp.sp1.m1_fn2("test")
        "sp1 m1 fn2 test"
        
    """

    return f"sp1 m1 fn2 {x}"
