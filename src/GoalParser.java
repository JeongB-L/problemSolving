public class GoalParser {

    public static String interpret(String command) {
        //replace every () into o, using replace() function.
        //replace every ( and ) into nothing using replace() function.
        // return the finale
        String finale = "";
        String newCommand = command.replace("()", "o");
        newCommand = newCommand.replace("(", "");
        finale = newCommand.replace(")", "");
        return finale;
    }

    public static void main(String[]args) {
        String example = "G()()()(al)";
        interpret(example);
    }
}
