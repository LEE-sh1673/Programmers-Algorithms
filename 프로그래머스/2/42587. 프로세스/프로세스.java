import java.util.LinkedList;
import java.util.Queue;


class Solution {

    public int solution(int[] priorities, int location) {
        Printer printer = new Printer(priorities);
        return printer.getOrder(location);
    }

    private static class Printer {

        private final Queue<Document> documents;

        public Printer(final int[] priorities) {
            this.documents = new LinkedList<>();
            for (int i = 0; i < priorities.length; i++) {
                documents.add(new Document(i, priorities[i]));
            }
        }

        public int getOrder(final int location) {
            int order = 0;

            while (!documents.isEmpty()) {
                final Document document = documents.poll();

                // 우선순위가 더 높은 프로세스가 존재
                if (!isGreatest(document.priority)) {
                    documents.offer(document);
                    continue;
                }

                // 대기 중인 프로세스를 꺼내는 경우
                order++;
                if (document.order == location) {
                    return order;
                }
            }
            return order;
        }

        private boolean isGreatest(final int priority) {
            return documents.stream().allMatch(doc -> doc.priority <= priority);
        }

        private static class Document {
            private final int order;
            private final int priority;

            public Document(final int order, final int priority) {
                this.order = order;
                this.priority = priority;
            }
        }
    }

}