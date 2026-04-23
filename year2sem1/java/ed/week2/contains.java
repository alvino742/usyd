public class contains {
	public static boolean contains(int[] a, int element) {
		if (a == null) {
			return false;
		}
		for (int item : a) {
			if (item == element) {
				return true;
			}
		}
		return false;
	}
	
	public static void main(String[] args) {
		int[] array = {1,2,3,4,5,6,7,7,8};

		boolean result = contains(array, 8);
		System.out.println(result);
	}
}
