import emoji

def main():
    prompt = emo(input("Input: "))
    print(f"Output: {prompt}")


def emo(prompt):
    try:
        emoji_text = emoji.emojize(prompt, language = "alias")
        return emoji_text
    except Exception as e:
        print(f"轉換過程出現錯誤: {e}")
        return prompt

if __name__ == "__main__":
    main()