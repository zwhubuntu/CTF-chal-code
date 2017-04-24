'''
#include<bits/stdc++.h>
using namespace std;

void f()
{
	string a;
	cin>>a;
	a[0]='H';
	string key="a7shw9o10e63nfi19dk";
	int l=a.length();
	char b[l+1];
	b[0]=a[0]^0x1;
	for(int i=1;i<l;i++)
	{
		char c=a[i]^b[i-1];
		b[i]=c;
	}
	for(int i=0;i<l-1;i++)
	{
		char c=b[i]^b[i+1];
		c=c^0x53;
		b[i]=c;
	}
	for(int i=1;i<=18;i++)
	{
		key[i]=key[i-1]^key[i]^a[(i-1)%7]^a[(i-1)%9];
	}
	for(int i=0;i<19;i++)
	{
		b[i]=b[i]^key[i];
	}
	char e[]={71,100,24,51,16,97,81,59,53,94,99,100,29,116,25,77,96,27,105};
	for(int i=0;i<l;i++)
	{
		if(b[i]!=e[i])
		{
			cout<<"failed"<<endl;
			return ;
		}
	}
	cout<<"successful"<<endl;
	for(int i=0;i<l;i+=2)
	{
		if(a[i]>=65&&a[i]<=90)
			a[i]+=32;
		if(a[i+1]>=97&&a[i+1]<=122)
			a[i+1]-=32;
	}
	cout<<"flag is: hbctf{"<<a<<"}"<<endl;
}
int main()
{
	f();
}


'''

key = "a7shw9o10e63nfi19dk"
target = [71, 100, 24, 51, 16, 97, 81, 59, 53, 94, 99, 100, 29, 116, 25, 77, 96, 27, 105]
