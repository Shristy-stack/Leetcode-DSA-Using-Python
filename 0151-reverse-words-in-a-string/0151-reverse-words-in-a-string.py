class Solution:
    def reverseWords(self, s: str) -> str:
        cleaned = re.sub(r"\s+", " ", s).strip()
        return " ".join(cleaned.split(" ")[::-1])