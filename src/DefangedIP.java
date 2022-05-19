public class DefangedIP {
    public String defangIPaddr(String address) {
        if (address.equals("")) {
            return address;
        }
        return address.replace(".", "[.]");
    }
}
