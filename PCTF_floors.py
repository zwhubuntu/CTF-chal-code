'''
Created on 2016-9-19

while(true) {
            if(this.to_reach_int < 0) {
                this.to_reach_int *= -1;
            }

            if(5 < this.to_reach_int) {
                this.to_reach_int %= 32;
                this.to_reach_int *= 16384;
                this.findViewById(2131492947).setText("" + this.to_reach_int);
                this.findViewById(2131492951).setText("");
                return;
            }

            this.to_reach_int = v1.nextInt();
        }

@author: wenhuizone
'''
v = 114688
