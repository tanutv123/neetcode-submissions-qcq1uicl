public class TimeMap {
    private Dictionary<string, List<Tuple<int, string>>> keyStore;
    public TimeMap() {
        keyStore = new Dictionary<string, List<Tuple<int, string>>>();
    }
    
    public void Set(string key, string value, int timestamp) {
        if(!keyStore.ContainsKey(key)) {
            keyStore[key] = new List<Tuple<int, string>>();
        }
        keyStore[key].Add(Tuple.Create(timestamp, value));
    }
    
    public string Get(string key, int timestamp) {
        if(!keyStore.ContainsKey(key)) {
            return "";
        }
        var values = keyStore[key];
        int l = 0, r = values.Count - 1;
        var res = "";
        while(l <= r) {
            int mid = (l + r) / 2;
            if(values[mid].Item1 <= timestamp) {
                res = values[mid].Item2;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return res;
    }
}
