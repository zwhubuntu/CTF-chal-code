'''
Created on 2016-3-29

@author: wenhuizone
'''
'''
            $data = mysql_fetch_array($result);
            if($pass == stringxor($key, base64_decode($data['member_password']))){
                                // authentication success
                                print "<p>Authentication success !!</p>";
                                if ($user == "admin")
                                    print "<p>Yeah !!! You're admin ! Use this password to complete this challenge.</p>";
                                else 
                                    print "<p>But... you're not admin !</p>";
$key = "c92fcd618967933ac463feb85ba00d5a7ae52842";

function stringxor($o1, $o2) {
    $res = '';
    for($i=0;$i<strlen($o1);$i++)
        $res .= chr(ord($o1[$i]) ^ ord($o2[$i]));        
    return $res;
}
'''

import base64

pwd='VA5QA1cCVQgPXwEAXwZVVVsHBgtfUVBaV1QEAwIFVAJWAwBRC1tRVA=='
key="c92fcd618967933ac463feb85ba00d5a7ae52842"

pwd_bsdecode=base64.b64decode(pwd)
result=''

for i in range(len(key)):
    result+=chr(ord(key[i])^ord(pwd_bsdecode[i]))
print result