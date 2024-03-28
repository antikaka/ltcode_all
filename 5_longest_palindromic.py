
"""
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

"""

# s = "bacabab"
# s = "abacab"
s = "abbcccbbbcaaccbababcbcabca"
# s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
# s = "eabcb"
# s = "wsgdzojcrxtfqcfkhhcuxxnbwtxzkkeunmpdsqfvgfjhusholnwrhmzexhfqppatkexuzdllrbaxygmovqwfvmmbvuuctcwxhrmepxmnxlxdkyzfsqypuroxdczuilbjypnirljxfgpuhhgusflhalorkcvqfknnkqyprxlwmakqszsdqnfovptsgbppvejvukbxaybccxzeqcjhmnexlaafmycwopxntuisxcitxdbarsicvwrvjmxsapmhbbnuivzhkgcrshokkioagwidhmfzjwwywastecjsolxmhfnmgommkoimiwlgwxxdsxhuwwjhpxxgmeuzhdzmuqhmhnfwwokgvwsznfcoxbferdonrexzanpymxtfojodcfydedlxmxeffhwjeegqnagoqlwwdctbqnuxngrgovrjesrkjrfjawknbrsfywljscfvnjhczhyeoyzrtbkvvfvofykkwoiclgxyaddhpdoztdhcbauaagjmfzkkdqexkczfsztckdlujgqzjyuittnudpldjvsbwbzcsazjpxrwfafievenvuetzcxynnmskoytgznvqdlkhaowjtetveahpjguiowkiuvikwewmgxhgfjuzkgrkqhmxxavbriftadtogmhlatczusxkktcsyrnwjbeshifzbykqibghmmvecwwtwdcscikyzyiqlgwzycptlxiwfaigyhrlgtjocvajcnqyenxrnjgogeqtvkxllxpuoxargzgcsfwavwbnktchwjebvwwhfghqkcjhuhuqwcdsixrkfjxuzvhjxlyoxswdlwfytgbtqbeimzzogzrlovcdpseoafuxfmrhdswwictsctawjanvoafvzqanvhaohgndbsxlzuymvfflyswnkvpsvqezekeidadatsymbvgwobdrixisknqpehddjrsntkqpsfxictqbnedjmsveurvrtvpvzbengdijkfcogpcrvwyf"

ilgiausias = ""
ss = s
for num, char in enumerate(s):
    if (len(s) - num) - len(ilgiausias) < 0:
        break
    print("dabar", char)
    if s.find(char) != s.rfind(char):
        print("check", char)
        s_list = list(s[num:])
        s_lcopy = s_list.copy()
        count = s_list.count(char)
        print(s_lcopy, "naujas ejimas")
        for num2 in range(count):
            print("num2", num2, "count=", count)
            ss = "".join(s_lcopy)
            if count > 0 and num2 < 1:
                count2 = len(ss) - (ss.rfind(char) + 1)
                print("reikia trint", count2)
                while count2 > 0:
                    print("istrinam", s_lcopy[-1])
                    s_lcopy.pop(-1)
                    count2 -= 1

            ss = "".join(s_lcopy)
            ss_rev = "".join(reversed(s_lcopy))
            print("tikrinu", ss, ss_rev)
            if ss == ss_rev and len(ilgiausias) < len(ss):
                ilgiausias = ss
                print("ilg", ilgiausias)
                if ss == ss_rev:
                    break
            ss = "".join(s_lcopy)
            count2 = len(ss) - (ss.rfind(char) + 1)
            print("reikia trint", count2)
            if count2 < 1:
                print("istrinam", s_lcopy[-1])
                s_lcopy.pop(-1)
            ss = "".join(s_lcopy)
            count2 = len(ss) - (ss.rfind(char) + 1)
            print("reikia trint", count2)
            ss = "".join(s_lcopy)
            while count2 > 0 and len(s_lcopy) > 2:
                print("istrinam", s_lcopy[-1])
                s_lcopy.pop(-1)
                count2 -= 1


print(ilgiausias)


