boms = {
    b"\xef\xbb\xbf",
    b"\xfe\xff",
    b"\xff\xfe",
    b"\x00\x00\xfe\xff",
    b"\xff\xfe\x00\x00",
}


def detectAndDeleteBomFromFile(filePath):
    with open(filePath, "rb") as f:
        data = f.read()

    for bom in boms:
        if data.startswith(bom):
            data = data[len(bom) :]
            break

    with open(filePath, "wb") as f:
        f.write(data)


def detectAndDeleteBom(data: bytes):
    for bom in boms:
        if data.startswith(bom):
            data = data[len(bom) :]
            break

    return data


def detectAndDeleteBomFromFileSaveTo(filePath, saveTo):
    try:
        with open(filePath, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"{filePath} was not found")
    except PermissionError:
        print(f"Permission denied {filePath}")
    except Exception as e:
        print(f"An error occurred {e}")

    for bom in boms:
        if data.startswith(bom):
            data = data[len(bom) :]
            break

    with open(saveTo, "wb") as f:
        f.write(data)
