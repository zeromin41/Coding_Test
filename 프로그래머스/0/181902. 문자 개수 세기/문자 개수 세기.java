class Solution {
    public int[] solution(String my_string) {
        int[] answer = new int[52];

        for (int i = 0; i < my_string.length(); i++) {
            char currentChar = my_string.charAt(i);

            if (currentChar >= 'A' && currentChar <= 'Z') {
                if (currentChar == 'A') {
                    answer[0]++;
                } else if (currentChar == 'B') {
                    answer[1]++;
                } else if (currentChar == 'C') {
                    answer[2]++;
                } else if (currentChar == 'D') {
                    answer[3]++;
                } else if (currentChar == 'E') {
                    answer[4]++;
                } else if (currentChar == 'F') {
                    answer[5]++;
                } else if (currentChar == 'G') {
                    answer[6]++;
                } else if (currentChar == 'H') {
                    answer[7]++;
                } else if (currentChar == 'I') {
                    answer[8]++;
                } else if (currentChar == 'J') {
                    answer[9]++;
                } else if (currentChar == 'K') {
                    answer[10]++;
                } else if (currentChar == 'L') {
                    answer[11]++;
                } else if (currentChar == 'M') {
                    answer[12]++;
                } else if (currentChar == 'N') {
                    answer[13]++;
                } else if (currentChar == 'O') {
                    answer[14]++;
                } else if (currentChar == 'P') {
                    answer[15]++;
                } else if (currentChar == 'Q') {
                    answer[16]++;
                } else if (currentChar == 'R') {
                    answer[17]++;
                } else if (currentChar == 'S') {
                    answer[18]++;
                } else if (currentChar == 'T') {
                    answer[19]++;
                } else if (currentChar == 'U') {
                    answer[20]++;
                } else if (currentChar == 'V') {
                    answer[21]++;
                } else if (currentChar == 'W') {
                    answer[22]++;
                } else if (currentChar == 'X') {
                    answer[23]++;
                } else if (currentChar == 'Y') {
                    answer[24]++;
                } else if (currentChar == 'Z') {
                    answer[25]++;
                }

            } else if (currentChar >= 'a' && currentChar <= 'z') {
                if (currentChar == 'a') {
                    answer[26]++;
                } else if (currentChar == 'b') {
                    answer[27]++;
                } else if (currentChar == 'c') {
                    answer[28]++;
                } else if (currentChar == 'd') {
                    answer[29]++;
                } else if (currentChar == 'e') {
                    answer[30]++;
                } else if (currentChar == 'f') {
                    answer[31]++;
                } else if (currentChar == 'g') {
                    answer[32]++;
                } else if (currentChar == 'h') {
                    answer[33]++;
                } else if (currentChar == 'i') {
                    answer[34]++;
                } else if (currentChar == 'j') {
                    answer[35]++;
                } else if (currentChar == 'k') {
                    answer[36]++;
                } else if (currentChar == 'l') {
                    answer[37]++;
                } else if (currentChar == 'm') {
                    answer[38]++;
                } else if (currentChar == 'n') {
                    answer[39]++;
                } else if (currentChar == 'o') {
                    answer[40]++;
                } else if (currentChar == 'p') {
                    answer[41]++;
                } else if (currentChar == 'q') {
                    answer[42]++;
                } else if (currentChar == 'r') {
                    answer[43]++;
                } else if (currentChar == 's') {
                    answer[44]++;
                } else if (currentChar == 't') {
                    answer[45]++;
                } else if (currentChar == 'u') {
                    answer[46]++;
                } else if (currentChar == 'v') {
                    answer[47]++;
                } else if (currentChar == 'w') {
                    answer[48]++;
                } else if (currentChar == 'x') {
                    answer[49]++;
                } else if (currentChar == 'y') {
                    answer[50]++;
                } else if (currentChar == 'z') {
                    answer[51]++;
                }
            }
        }
        return answer;
    }
}