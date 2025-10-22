def dedupe_list(input_list: list) -> list:
    """Remove duplicates from a list while preserving order"""
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# 测试入口（可选，方便本地运行）
if __name__ == "__main__":
    sample_list = [1, 2, 2, 3, 4, 4, 4, 5]
    print(f"Original list: {sample_list}")
    print(f"Deduped list: {dedupe_list(sample_list)}")