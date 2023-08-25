def get_nodes(nodes: list[str] | None) -> None:
    if not nodes:
        print("no nodes")
    print(nodes)


if __name__ == "__main__":
    get_nodes([])
