class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return '\x00'
        return '\x00'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '\x00': return []
        return s.split('\x00')
