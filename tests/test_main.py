import asyncio


def test_main():
    from fireset.web import main_web_run

    asyncio.run(
        main_web_run(
            defaults=True,
            directory="/home/yann/Downloads/xandikos_data",
            port=3665,
            autocreate=True,
        )
    )


if __name__ == "__main__":
    test_main()
