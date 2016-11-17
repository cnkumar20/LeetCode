package LeetCode;

public class LargestNumber {
    public String largestNumber(int[] nums) {
		if(nums==null || nums.length==0) {
			return "";
		}
		StringBuffer sb = new StringBuffer();	
		String[] stringNum = new String[nums.length];			
		int j = 0;		
		for (int i : nums) {
			stringNum[j++] = String.valueOf(i);
		}
		Arrays.sort(stringNum,new StringComparator());
		for(String x : stringNum) {
			sb.append(x);
		}
		if (sb.charAt(0) == '0') {
            return "0";
        }
		return sb.toString();
	}
	public class StringComparator implements Comparator<String> {
        @Override
        public int compare (String str1, String str2) {
        String ab = str1 + str2;
        String ba = str2 + str1;
        return ba.compareTo(ab);
        }
    }
}
