import { View, Text } from 'react-native';

export default function LittleLemonHeader() {
  return (
    <View style={{ flex: 0.15, backgroundColor: '#F4CE14' }}>
      <Text
        style={{
          padding: 40,
          fontSize: 30,
          color: 'black',
          textAlign: 'center',
        }}>
        Little Lemon 
        Contact informations :
        Phone number  +1 347 797 0944
        Email         littleLemon@amail.com
        All rights reserved by Little Lemon, 2022
      </Text>
    </View>
  );
}
