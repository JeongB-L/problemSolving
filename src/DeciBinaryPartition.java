public class DeciBinaryPartition {
    public int minPartitions(String n) {
        //결과적으로 여러 숫자중에 가장 높은 숫자의 자릿수가 결정한다
        int finale = 0;
        for (int i = 0; i < n.length(); i++) {
            finale = Math.max(finale, n.charAt(i) - '0');
        }
        return finale;
    }
}
