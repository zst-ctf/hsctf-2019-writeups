public class MyClass {
    static String solve_flag() {
        char[] ret_val = "\uffc8\uffbd\uffce\uffbc\uffca\uffb7\uffc5\uffcb\u0005\uffc5\uffd5\uffc1\uffff\uffc1\uffd8\uffd1\uffc4\uffcb\u0010\uffd3\uffc4\u0001\uffbf\uffbf\uffd1\uffc0\uffc5\uffbb\uffd5\uffbe\u0003\uffca\uffff\uffda\uffc3\u0007\uffc2\u0001\uffd4\uffc0\u0004\uffbe\uffff\uffbe\uffc1\ufffd\uffb5".toCharArray();
        char[] heck = "001002939948347799120432047441372907443274204020958757273".toCharArray();
        
        int flag_length = ret_val.length;
        char[] flag = new char[flag_length];
        
        // flag[i] = heck[i] + ret_val[i]
        for (int i = 0; i < flag_length; i++) {
            flag[i] = (char) (heck[i] - ret_val[i]);
        }
        
        return new String(flag);
    }

    public static void main(String args[]) {
        System.out.println(solve_flag());
    }
}
