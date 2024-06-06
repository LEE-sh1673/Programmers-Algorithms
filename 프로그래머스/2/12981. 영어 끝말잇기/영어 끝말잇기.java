import java.util.*;


class Solution {
    
    public int[] solution(int n, String[] words) {
        final WorkRelayGame game = new WorkRelayGame(n);
        return game.play(words);
    }

    static class WorkRelayGame {

        private final List<RelayWord> relayWords;
        private final int numberOfPeople;

        WorkRelayGame(final int numberOfPeople) {
            this.relayWords = new ArrayList<>();
            this.numberOfPeople = numberOfPeople;
        }

        int[] play(final String[] words) {
            final int[] result = new int[2];

            for (int i = 0; i < words.length; i++) {
                final RelayWord word = new RelayWord(i, words[i], numberOfPeople);

                if (!isValidWord(word) || !tryWord(word)) {
                    result[0] = word.getNo();
                    result[1] = word.getOrder();
                    break;
                }
            }
            return result;
        }

        boolean isValidWord(final RelayWord word) {
            if (relayWords.isEmpty()) {
                return true;
            }
            RelayWord prevWord = relayWords.get(relayWords.size() - 1);
            return prevWord.getLastCharacter() == word.getFirstCharacter();
        }

        boolean tryWord(final RelayWord word) {
            if (relayWords.contains(word)) {
                return false;
            }
            return relayWords.add(word);
        }
    }

    static class RelayWord {

        private int no;
        private String word;
        private int numberOfPeople;

        RelayWord(final int no, final String word, final int numberOfPeople) {
            this.no = no;
            this.word = word;
            this.numberOfPeople = numberOfPeople;
        }

        int getNo() {
            return no % numberOfPeople + 1;
        }

        int getOrder() {
            return no / numberOfPeople + 1;
        }

        char getFirstCharacter() {
            return word.charAt(0);
        }

        char getLastCharacter() {
            return word.charAt(word.length() - 1);
        }

        @Override
        public boolean equals(final Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()) {
                return false;
            }
            final RelayWord other = (RelayWord) o;
            return Objects.equals(word, other.word);
        }

        @Override
        public int hashCode() {
            return Objects.hash(word);
        }
    }
}
