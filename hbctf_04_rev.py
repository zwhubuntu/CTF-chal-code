# coding:utf-8
'''
private void 关于ToolStripMenuItem_Click(object sender, EventArgs e)
{
    string s = "Maybe God wants us to meet a few wrong people before meeting the right one,";
    s = s + "so that when we finally meet the person," + "we will know how to be grateful.";
    string str2 = "aGJjdGZ7";
    byte[] bytes = Convert.FromBase64String(str2);
    string str3 = Encoding.Default.GetString(bytes);
    byte[] buffer2 = MD5.Create().ComputeHash(Encoding.UTF8.GetBytes(s));
    for (int i = 0; i < buffer2.Length; i++)
    {
        str3 = str3 + buffer2[i].ToString("x");
    }
    str3 = str3 + char.ConvertFromUtf32(0x7d);
    MessageBox.Show(s, "pcat@chamd5.org");
}


'''
import hashlib

s = "Maybe God wants us to meet a few wrong people before meeting the right one,so that when we finally meet the person,we will know how to be grateful."
strr = hashlib.md5(s).hexdigest()
print strr
# 1a117eef02eae51ca27c35d42b37defa
str =
