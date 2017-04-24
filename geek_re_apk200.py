'''
public void appInit() {
        this.btnCheck = this.findViewById(2131492945);
        this.usrName = this.findViewById(2131492950);
        this.usrPass = this.findViewById(2131492949);
        this.keyShow = this.findViewById(2131492946);
        this.keyShow.setText("Have FUN With GeekChal2016");
    }

    public boolean checkInput(EditText name, EditText pass) {
        boolean v0;
        if((name.getText().toString().isEmpty()) || (pass.getText().toString().isEmpty())) {
            v0 = false;
        }
        else {
            v0 = true;
        }

        return v0;
    }

    public void onClick(View view) {
        switch(view.getId()) {
            case 2131492945: {
                goto label_4;
            }
        }

        return;
    label_4:
        if(!this.checkInput(this.usrName, this.usrPass)) {
            goto label_49;
        }

        if(this.usrName.getText().toString().length() != 16) {
            goto label_44;
        }

        Handler v2 = new Handler(this.usrName.getText().toString(), this.usrPass.getText().toString(
                ));
        v2.handleInput();
        new AESEncrpty();
        try {
            if(!v2.getPass().equals(AESEncrpty.Encrypt(v2.getName(), v2.getNameCalc()))) {
                goto label_38;
            }

            Toast.makeText(this.getApplicationContext(), "Yes", 0).show();
            return;
        label_38:
            Toast.makeText(this.getApplicationContext(), "retry...", 0).show();
            return;
        }
        catch(Exception v1) {
            v1.printStackTrace();
            return;
        }

    label_44:
        Toast.makeText(this.getApplicationContext(), "retry...", 0).show();
        return;
    label_49:
        Toast.makeText(this.getApplicationContext(), "Plz input sth...", 0).show();
    }

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.setContentView(2130968601);
        this.appInit();
        this.btnCheck.setOnClickListener(((View$OnClickListener)this));
    }
}
        String v4 = null;
        if(sKey != null && sKey.length() == 16) {
            SecretKeySpec v3 = new SecretKeySpec(sKey.getBytes("utf-8"), "AES");
            Cipher v0 = Cipher.getInstance("AES/ECB/PKCS5Padding");
            v0.init(1, ((Key)v3));
            v4 = Base64.encodeToString(v0.doFinal(sSrc.getBytes("utf-8")), 0);
        }
char[] str = this.str.toCharArray();
        int i;
        for(i = 0; i < array.length; ++i) {
            array[i] = ((char)(array[i] + 3));
        }

        int v6;
        for(v6 = 0; true; ++v6) {
            if(v6 >= array.length) {
                goto label_31;
            }

            v8[v6] = str[array[v6] % str.length];
        }

v8[v6] = str[username[v6] % str.length];

    public encrpty2() {
        super();
        this.xorString = "o0xmuhe";
        this.str = "talkischeapshowmethecode$ischeapshowmethe#SycSYC{IamNotFLAG2333}";
    }
for(v0 = 0; v0 < v8.length; ++v0) {
            v2[v0] = v8[v0] ^ v6[v0 % 7];
        }

        int v1;
        for(v1 = 0; v1 < v8.length; ++v1) {
            v3[v1] = v5[(v2[v1] + 7) % v5.length];
        }
'''
import base64

from Crypto.Cipher import AES

encrypt1_str = "ThisIsNotFL@GplzDonnotSubmitThisString#HaveFunWithGeekmastergogo"
username_handle1 = ''
v8 = ''
v2 = []
v8_handle = ''
username_handle = ''
xor_string = 'o0xmuhe'
encrypt2_str = "talkischeapshowmethecode$ischeapshowmethe#SycSYC{IamNotFLAG2333}"
username = '1' * 16
'''
padding writing
'''
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

for j in username:
    username_handle += chr(ord(j) + 3)
print "first_handle is: %s"%(username_handle)
for i in xrange(len(username)):
    v8 += encrypt1_str[ord(username_handle[i]) % len(encrypt1_str)]
for k in xrange(len(v8)):
    v2.append(ord(v8[k]) ^ ord(xor_string[k % 7]))
for l in xrange(len(v8)):
    v8_handle += encrypt2_str[(v2[l] + 7) % len(encrypt2_str)]
key = v8_handle[::-1]
print "the key is:%s" %(key)
mode = AES.MODE_ECB
enc = AES.new(key, mode)
ciper = base64.b64encode(enc.encrypt(pad(username)))
print "the username is: %s" % username
print "the password is %s" %ciper




