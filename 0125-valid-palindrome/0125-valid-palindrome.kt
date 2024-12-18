class Solution {
    fun isPalindrome(s: String): Boolean {
        val s2 = s.filter { it.isLetterOrDigit() }.map { it.lowercase() }.joinToString("")
        val answer: Boolean = s2 == s2.reversed()

        return answer
    }
}