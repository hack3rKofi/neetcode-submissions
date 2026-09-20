func isAnagram(s string, t string) bool {

    if len(t) != len(s){
        return false
    }

    count := [26]int{}
    for i := 0; i < len(s); i++{
        count[s[i]-'a']++
        count[t[i]-'a']--
    }

    for _, val := range count{
        if val != 0{
            return false
        }
    }

    return true
}
