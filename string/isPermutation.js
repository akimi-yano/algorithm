function isPermutation(str1, str2) {
    if (!(str1.length === str2.length)) {
        return false
    }
    let dict1={}
    let dict2={}
    let news1=str1.toLowerCase();
    let news2 = str2.toLowerCase();
    for (let i = 0; i < news1.length; i++) {
        if(news1[i] in dict1){
            dict1[news1[i]]+=1
        }
        else{
            dict1[news1[i]]=1
        }
    }

    for (let k = 0; k < news2.length; k++) {
        if(news2[k] in dict2){
            dict2[news2[k]]+=1
        }
        else{
            dict2[news2[k]]=1
        }
    }

    for (property in dict1) {

        if (dict1[property] !== dict2[property]) {
            return false
        }
    }
    return true
}
console.log(isPermutation("abc","cAb"))

