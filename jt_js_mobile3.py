'''
package ctf.bobbydylan;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;

public class M extends T {
    public M() {
        super();
    }

    public void check(String arg10) {
        String v0_1;
        int v7 = 15;
        int v6 = 7;
        int v1 = 0;
        int v5 = 5;
        if(arg10.length() == 16) {
            goto label_11;
        }

        throw new RuntimeException();
        try {
        label_11:
            v0_1 = this.getKey();
        }
        catch(Exception v0) {
            v0_1 = this.getKey();
            System.arraycopy(v0_1, 0, arg10, v5, v5);
        }

        int[] v2 = new int[16];
        v2[0] = 42;
        v2[12] = 14;
        v2[10] = v6;
        v2[14] = v7;
        v2[v7] = 17;
        int v4 = 43;
        try {
            v2[1] = v4;
            v2[5] = 5;
            System.out.println();
        }
        catch(Exception v3) {
            v2[v5] = 37;
            v2[1] = 85;
        }

        v2[6] = v7;
        v2[2] = 32;
        v2[3] = 23;
        v2[11] = 68;
        v2[4] = 85;
        v2[13] = v5;
        v2[9] = v6;
        v2[v6] = 8;
        v2[8] = 22;
        while(v1 < arg10.length()) {
            if((v2[v1] & 255) != ((arg10.charAt(v1) ^ v0_1.charAt(v1 % v0_1.length())) & 255)) {
                throw new RuntimeException();
            }

            ++v1;
        }
    }

    public String getKey() {
        return "AnyLab";
    }

    public void onCreate(Bundle arg4) {
        super.onCreate(arg4);
        this.setContentView(2130903040);
        this.startService(new Intent(((Context)this), P.class));
        this.findViewById(2131099649).setOnClickListener(new a(this, this.findViewById(2131099648)))
                ;
    }

    protected void onPause() {
        this.stopService(new Intent(((Context)this), P.class));
        super.onPause();
    }
}


'''
