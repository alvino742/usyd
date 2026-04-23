public class ArrayMerge {
	public static int[][] mergeArrays(int[][] arrayA, int[][] arrayB){
		if (arrayA == null || arrayB == null) {
			return null;
		}

		int rows = arrayA.length;
		int colA = arrayA[0].length;
		int colB = arrayB[0].length;
		int[][] arrayC = new int[rows][colA + colB];

		for (int i = 0; i < rows; i++){
			for (int j = 0; j < colA; j++){
				arrayC[i][j] = arrayA[i][j];
			}
			for (int k = 0; k < colB; k++){
				arrayC[i][colA + k] = arrayB[i][k];
			}
		}

		return arrayC;

	}

	public static void main(String[] args){
		int[][] A = {{1,2,3,3},{3,2,1,6}, {4,5,6,1}};
		int[][] B = {{1,9,7,2,3},{0,7,8,3,2}, {3,8,9,7,2}};

		int[][] C = mergeArrays(A, B);
		for (int i = 0; i < C.length; i++){
			for (int j = 0; j < C[0].length; j++) {
				System.out.print(C[i][j]);
				System.out.print(" ");
			}
			System.out.print("\n");
		}
	}
}
