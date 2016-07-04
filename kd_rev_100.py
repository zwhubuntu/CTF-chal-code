'''
  public void onCreate(Bundle paramBundle)
  {
    super.onCreate(paramBundle);
    setContentView(2130903040);
    this.click = ((Button)findViewById(2131034112));
    this.showFlag = ((TextView)findViewById(2131034113));
    this.click.setOnClickListener(new View.OnClickListener()
    {
      public void onClick(View paramAnonymousView)
      {
        MyActivity.this.ctext[(MyActivity.this.count % MyActivity.this.textLen)] 
        = ((char)(MyActivity.this.ctext[(MyActivity.this.count % MyActivity.this.textLen)] ^ MyActivity.this.key[(MyActivity.this.count % MyActivity.this.keyLen)]));
        MyActivity.access$108(MyActivity.this);
        if (MyActivity.this.count == 50000)
        {
          MyActivity.this.showFlag.setText(String.valueOf(MyActivity.this.ctext));
          return;
        }
        MyActivity.this.showFlag.setText("count:" + MyActivity.this.count);
      }
    });
  }
}

@author: wenhuizone
'''
ctext=[61, 54, 40, 45, 48, 53, 39, 33, 16, 125, 34, 11, 13, 57, 33, 13, 23, 57, 100, 55, 97]
key=[65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
clen=len(ctext)
klen=len(key)
result=''
for i in range(0,50000):
    ctext[i%clen]=ctext[i%clen]^key[i%klen]
for j in ctext:
    result+=chr(j)
print result
