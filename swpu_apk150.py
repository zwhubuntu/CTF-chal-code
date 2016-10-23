'''
package com.example.test1;

import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View$OnClickListener;
import android.widget.Toast;

public class MainActivity extends Activity {
    String Flag;
    String encode;
    String encode1;
    int flag;

    public MainActivity() {
        super();
        this.Flag = "";
        this.flag = 0;
    }

    public String Encode1(String Flag, int len) {
        String v5;
        int v7 = 16;
        char[] v4 = Flag.toCharArray();
        int v2 = 29;
        int[] v0 = new int[v7];
        if(len == v7) {
            int v1;
            for(v1 = 0; v1 < Flag.length(); ++v1) {
                v0[v1] = v4[v1];
                v0[v1] ^= v2;
            }

            for(v1 = 1; v1 < 8; ++v1) {
                v0[v1] = v0[15 - v1];
                v0[15 - v1] = v0[v1];
            }

            for(v1 = 0; v1 < v7; ++v1) {
                v4[v1] = ((char)v0[v1]);
            }

            v5 = String.valueOf(v4);
        }
        else {
            v5 = "lalalalalalala~~";
        }

        return v5;
    }

    public String Encode2(String encode, String Flag) {
        char[] v1 = encode.toCharArray();
        char[] v2 = Flag.toCharArray();
        int v0;
        for(v0 = 0; v0 < 16; ++v0) {
            if(v0 % 2 == 0) {
                v1[v0] = v2[v0];
            }
        }

        return String.valueOf(v1);
    }

    public int chack(String encode1) {
        int v4;
        int v6 = 16;
        char[] v3 = encode1.toCharArray();
        int[] v1 = new int[v6];
        int[] v2 = new int[]{73, 48, 109, 97, 115, 46, 95, 116, 105, 111, 51, 89, 124, 73, 45, 73};
        int v0 = 0;
        while(true) {
            if(v0 < v6) {
                v1[v0] = v3[v0];
                if(v1[v0] != v2[v0]) {
                    v4 = 0;
                }
                else {
                    ++v0;
                    continue;
                }
            }
            else {
                break;
            }

            goto label_7;
        }

        v4 = 1;
    label_7:
        return v4;
    }

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.setContentView(2130903040);
        this.findViewById(2131230720).setOnClickListener(new View$OnClickListener() {
            public void onClick(View v) {
                MainActivity.this.Flag = MainActivity.this.findViewById(2131230721).getText().toString
                        ();
                if(MainActivity.this.Flag.length() != 16) {
                    Toast.makeText(MainActivity.this, "something wrong~~", 0).show();
                }
                else {
                    MainActivity.this.encode = MainActivity.this.Encode1(MainActivity.this.Flag, MainActivity
                            .this.Flag.length());
                    MainActivity.this.encode1 = MainActivity.this.Encode2(MainActivity.this.encode,
                            MainActivity.this.Flag);
                    MainActivity.this.flag = MainActivity.this.chack(MainActivity.this.encode1);
                    if(MainActivity.this.flag == 1) {
                        Toast.makeText(MainActivity.this, "WOw~, You got it !", 0).show();
                    }
                    else {
                        Toast.makeText(MainActivity.this, "trg again~", 0).show();
                    }
                }
            }
        });
    }

    public boolean onCreateOptionsMenu(Menu menu) {
        this.getMenuInflater().inflate(2131165184, menu);
        return 1;
    }

    public boolean onOptionsItemSelected(MenuItem item) {
        boolean v1;
        if(item.getItemId() == 2131230722) {
            v1 = true;
        }
        else {
            v1 = super.onOptionsItemSelected(item);
        }

        return v1;
    }
}

'''
import string
lst = string.printable.strip()
target = [73, 48, 109, 97, 115, 46, 95, 116, 105, 111, 51, 89, 124, 73, 45, 73]
swpu_flag = ''
encode1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
encode2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in xrange(16):
    for j in lst:
        if i == 0 or i == 15:
            tmp = j
            encode1[i] = ord(tmp) ^ 29
            if i % 2 == 0:
                encode2[i] = ord(tmp)
            else:
                encode2[i] = encode1[i]
            if encode2[i] == target[i]:
                swpu_flag += j
                break
        else:
            tmp = j
            encode1[i] = ord(tmp) ^ 29
            encode1[15 - i] = encode1[i]
            if i % 2 == 0:
                encode2[i] = ord(tmp)
            else:
                encode2[i] = encode1[i]
            if encode2[i] == target[i]:
                swpu_flag += j
                break
print "flag is %s" %swpu_flag


