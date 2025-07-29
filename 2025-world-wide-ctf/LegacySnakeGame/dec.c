#include <stdint.h>

uint64_t verify_license(uint64_t *data, int *chunk_count, uint64_t key) {
    uint64_t result;
    
    if (*chunk_count <= 1) {
        return 0; // Return early if not enough chunks
    }
    
    int rounds = 52 / *chunk_count + 6;
    uint64_t sum = 0;
    uint64_t prev = data[*chunk_count - 1];
    
    for (int round = 0; round < rounds; round++) {
        sum += 0x9E3779B9ULL; // TEA delta constant
        uint8_t e = (sum >> 2) & 3;
        
        // Process all chunks except the last one
        for (int i = 0; i < *chunk_count - 1; i++) {
            uint64_t next = data[i + 1];
            uint64_t key_offset = ((i ^ e) & 3) * 8;
            uint64_t *key_ptr = (uint64_t *)(key + key_offset);
            
            data[i] += ((sum ^ next) + (prev ^ *key_ptr)) ^ 
                       (((prev >> 5) ^ (next << 2)) + ((next >> 3) ^ (prev << 4)));
            prev = data[i];
        }
        
        // Process the last chunk
        int last_idx = *chunk_count - 1;
        uint64_t key_offset = ((last_idx ^ e) & 3) * 8;
        uint64_t *key_ptr = (uint64_t *)(key + key_offset);
        
        data[last_idx] += ((sum ^ data[0]) + (prev ^ *key_ptr)) ^ 
                          (((prev >> 5) ^ (data[0] << 2)) + ((data[0] >> 3) ^ (prev << 4)));
        
        result = data[last_idx];
        prev = result;
    }
    
    return result;
}


uint64_t decrypt_license(uint64_t *data, int *chunk_count, uint64_t key) {
    uint64_t result;
    
    if (*chunk_count <= 1) {
        return 0; // Return early if not enough chunks
    }
    
    int rounds = 52 / *chunk_count + 6;
    uint64_t sum = 0x9E3779B9ULL * rounds; // Start with final sum value
    uint64_t next = data[0];
    
    for (int round = 0; round < rounds; round++) {
        uint8_t e = (sum >> 2) & 3;
        
        // Process the last chunk first (reverse order)
        int last_idx = *chunk_count - 1;
        uint64_t key_offset = ((last_idx ^ e) & 3) * 8;
        uint64_t *key_ptr = (uint64_t *)(key + key_offset);
        uint64_t prev = (last_idx == 0) ? data[last_idx] : data[last_idx - 1];
        
        data[last_idx] -= ((sum ^ data[0]) + (prev ^ *key_ptr)) ^ 
                          (((prev >> 5) ^ (data[0] << 2)) + ((data[0] >> 3) ^ (prev << 4)));
        
        // Process all other chunks in reverse order
        for (int i = *chunk_count - 2; i >= 0; i--) {
            uint64_t current = data[i];
            next = data[i + 1];
            prev = (i == 0) ? data[last_idx] : data[i - 1];
            
            key_offset = ((i ^ e) & 3) * 8;
            key_ptr = (uint64_t *)(key + key_offset);
            
            data[i] -= ((sum ^ next) + (prev ^ *key_ptr)) ^ 
                       (((prev >> 5) ^ (next << 2)) + ((next >> 3) ^ (prev << 4)));
        }
        
        sum -= 0x9E3779B9ULL; // Subtract delta constant
        result = data[*chunk_count - 1];
    }
    
    return result;
}


int64_t uint64_to_hex(uint64_t *input_array, int length, char *output_buffer, int64_t output_length) {
    int64_t result;
    int i;
    
    // Initialize output buffer
    output_buffer[0] = '\0';
    
    for (i = 0; ; ++i) {
        result = (unsigned int)(8 * length);
        if (i >= (int)result)
            break;
        
        // Convert each byte to 2-character hex representation
        snprintf(&output_buffer[2 * i], output_length - 2 * i, "%02X", 
                 *((unsigned char*)input_array + i));
    }
    
    return result;
}


int64_t hex_to_uint64(const char *hex_string, uint64_t *output_array, int max_length) {
    int hex_len = strlen(hex_string);
    int byte_count = hex_len / 2;
    int uint64_count = (byte_count + 7) / 8;  // Round up to nearest uint64_t
    
    if (uint64_count > max_length) {
        return -1;  // Not enough space in output array
    }
    
    // Initialize output array to zero
    for (int i = 0; i < uint64_count; i++) {
        output_array[i] = 0;
    }
    
    // Convert hex string back to bytes
    for (int i = 0; i < byte_count; i++) {
        unsigned int byte_val;
        sscanf(&hex_string[i * 2], "%02X", &byte_val);
        
        // Place byte in appropriate uint64_t position
        int uint64_index = i / 8;
        int byte_position = i % 8;
        output_array[uint64_index] |= ((uint64_t)byte_val) << (byte_position * 8);
    }
    
    return uint64_count;  // Return number of uint64_t values filled
}

int main() {
    uint64_t dest[4];
    char* s = "there_is_no_such_free_lunch";
    memset(dest, 0, sizeof(dest));
    int v0 = strlen("there_is_no_such_free_lunch");
    memcpy(dest, "there_is_no_such_free_lunch", v0);

    // uint64_t data[] = {11217688877128249394, 12480011680869948127, 16698686595710974502, 15045632504118445585, 10805849222012673793, 15470718551566116912, 8834406881595145286, 6846913908997696794, 8220605163934775773, 850379994024257039};
    // uint64_t len = 10;

    // verify_license(data,&len,dest);
    // for (uint64_t i = 0; i < 10; i++){
    //     printf("%llu\n",data[i]);
    // }
    
    // printf("==========\n");

    // decrypt_license(data,&len,dest);
    // for (uint64_t i = 0; i < 10; i++){
    //     printf("%llu\n",data[i]);
    // }

    // // printf("==========\n");

    // char out[160] = {};
    // uint64_to_hex(data,10,out,160);
    // printf("%s\n",out);
    char* v10 = "73A1A5796D9483C29AD1580278B022DA55208AD1B1F834CA037C266B1C17AE5268B98191A95BBD7F2F976C64E8BD2D86F7CB17BAF1BDAC3FD322FC7235A32D48";

    uint64_t restored_data[10];
    uint64_t len = 8;
    hex_to_uint64(v10,restored_data,len);
    for (uint64_t i = 0; i < 10; i++){
        printf("%llu\n",restored_data[i]);
    }


    
    printf("==========\n");
// 
    decrypt_license(restored_data,&len,dest);
    for (uint64_t i = 0; i < 10; i++){
        printf("%llu\n",restored_data[i]);
    }    
}

