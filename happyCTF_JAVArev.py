# '''public class Reverse
# {
#   public Reverse() {}
#
#   public static void main(String[] args) {
#     java.util.Scanner s = new java.util.Scanner(System.in);
#     System.out.println("Please input the flag ：");
#     String str = s.next();
#     System.out.println("Your input is ：");
#     System.out.println(str);
#     char[] stringArr = str.toCharArray();
#     Encrypt(stringArr);
#   }
#
#   public static void Encrypt(char[] arr) {
#     ArrayList<Integer> Resultlist = new ArrayList();
#
#     for (int i = 0; i < arr.length; i++) {
#       int result = arr[i] + '@' ^ 0x20;
#       Resultlist.add(Integer.valueOf(result));
#     }
#     int[] KEY = { 180, 136, 137, 147, 191, 137, 147, 191, 148, 136, 133, 191, 134, 140, 129, 135, 191, 65 };
#     ArrayList<Integer> KEYList = new ArrayList();
#     for (int j = 0; j < KEY.length; j++) {
#       KEYList.add(Integer.valueOf(KEY[j]));
#     }
#     System.out.println("Result:");
#     if (Resultlist.equals(KEYList)) {
#       System.out.println("Congratulations！");
#     } else {
#       System.err.println("Error！");
#     }
#   }
# }
#
#
#
key = [180, 136, 137, 147, 191, 137, 147, 191, 148, 136, 133, 191, 134, 140, 129, 135, 191, 65]

flag = ''

for i in xrange(len(key)):
    flag += chr(key[i] - ord('@') ^ 0x20)

print flag
