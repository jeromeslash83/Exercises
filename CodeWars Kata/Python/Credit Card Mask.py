def maskify(cc):
    length = len(cc)
    if length > 4:
        last_char = cc[-4:]
        return  f"{'#' * (length-4)}{last_char}"
    else:
        return cc
