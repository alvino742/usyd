import java.util.*;
import java.io.*;

public class FileParser {
	public static void main(String[] args) {
		try (Scanner scanner = new Scanner(new File("items.txt"))) {
			while (scanner.hasNextLine()) {
				String line = scanner.nextline().trim();
				if (line.isEmpty()) continue;

				String[] parts = line.split(":");
				if (parts.length == 2) {
					String items = parts[0];
					int quantity = Integer.parseInt(parts[1]);
				}
			}
		}
	}
}
