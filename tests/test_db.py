from fireset.database import get_vcard


if __name__ == "__main__":
    # for c in list_vcards():
    #     print(c)
    #     break

    c = get_vcard(52)
    print(c.toVcard().decode("utf-8"))
