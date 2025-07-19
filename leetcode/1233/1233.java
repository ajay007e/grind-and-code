class Solution {
    public List<String> removeSubfolders(String[] folders) {
       Arrays.sort(folders);
       ArrayList<String> res = new ArrayList<String>();
       for(String path : folders) {
            if (res.size() != 0 && path.startsWith(res.get(res.size() - 1).concat("/")) == true) {
                continue;
            } else{
                res.add(path);
            }
       }
       return res;
    }
}
