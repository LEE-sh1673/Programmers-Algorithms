import java.util.LinkedList;
import java.util.Queue;


public class Printer {

    private final Queue<Document> documents;


    private static class Document {

        private final int order;
        private final int priority;

        public Document(final int order, final int priority) {
            this.order = order;
            this.priority = priority;
        }
    }

    public Printer(int[] priorities) {
        this.documents = new LinkedList<>();
        mapDocuments(priorities);
    }

    private void mapDocuments(final int[] priorities) {
        for (int i = 0; i < priorities.length; i++) {
            documents.offer(new Document(i, priorities[i]));
        }
    }

    public int getOrder(final int location) {
        int order = 0;

        while (true) {
            Document document = documents.poll();

            if (isGreaterThen(document)) {
                documents.offer(document);
            } else {
                order++;
                if (matchOrder(location, document)) {
                    return order;
                }
            }
        }
    }


    private static boolean matchOrder(final int location, final Document document) {
        return document != null && document.order == location;
    }

    private boolean isGreaterThen(final Document document) {
        return document != null && documents.stream()
            .anyMatch(doc -> doc.priority > document.priority);
    }
}



class Solution {
    public int solution(int[] priorities, int location) {
        Printer printer = new Printer(priorities);
        return printer.getOrder(location);
    }
}