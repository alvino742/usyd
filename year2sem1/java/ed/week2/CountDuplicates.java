import java.util.ArrayList;

public class CountDuplicates {
	public static int countDuplicates(int[] a){
		if (a == null) {
			return 0;
		}
		int length = a.length;
		int dups = 0;
		ArrayList<Integer> duplicated = new ArrayList<>();
		for (int i = 0; i < length; i++){
			boolean dup = false;
			for (int k = 0; k < duplicated.size(); k++) {
				if ((duplicated.get(k).equals(i))) {
					dup = true;
					break;
				}
			}
			if (!dup) {
				boolean duplication = false;
				for (int j = 0; j < length; j++) {
					if (i == j) continue;
					if (a[i] == a[j]) {
						duplication = true;
						duplicated.add(j);
					}
				}
				if (duplication) dups++;
			}
		}
		return dups;
	}
}
