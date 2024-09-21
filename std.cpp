#include <bits/stdc++.h>
using namespace std;

int a[100010];
int mp[1000010];

int main(){
    int n;
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>a[i];
        mp[a[i]]++;
    }
    int ans=0;
    for(int i=1;i<=1000000;i++){
        if(mp[i]==0)continue;
        if(mp[i]<2){
            cout<<"-1"<<endl;
            return 0;
        }
        int tmp2=floor(1.0*(mp[i])/3);
        while(tmp2>=0){
            int tmp1=floor(1.0*(mp[i]-tmp2*3)/2);
            if(tmp2*3+tmp1*2==mp[i]){
                ans=ans+tmp1+tmp2;
                break;
            }
            tmp2--;
        }
    }
    cout<<ans<<endl;
    return 0;
}
