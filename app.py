import streamlit as st
import pandas as pd
import numpy as np

def init_db():
    map_question_to_answer = [
        {
            "ques": "1. Bạn sử dụng phương tiện gì để sử dụng ứng dụng CNTT trong học tập?",
            "choice": "Máy tính để bàn;Laptop;Điện thoại;Máy tính bảng;Tivi",
            "p": "0.1;0.3;0.4;0.1;0.1",
            "one_choice": False
        },
        {
            "ques": "2. Ứng dụng CNTT nào được bạn sử dụng để hỗ trợ học tập?",
            "choice": "Google;Youtube;Chat GPT;Thư viện điện tử;Dạy học kết hợp;Facebook;Zalo;Instagram;Tiktok",
            "p": "0.2;0.1;0.1;0.1;0.1;0.1;0.1;0.1;0.1",
            "one_choice": False
        },
        {   
            "ques": "3. Mục đích sử dụng ứng dụng CNTT trong học tập của bạn là gì?",
            "choice": "Tìm kiếm thông tin, tài liệu tham khảo;Tìm câu trả lời, đáp án;Đạt điểm số cao;Gian lận trong học tập",
            "p": "0.4;0.3;0.2;0.1",
            "one_choice": False
        },
        {
            "ques": "4. Thời gian sử dụng trung bình các ứng dụng CNTT trong một ngày cho mục đích học tập của bạn?",
            "choice": "Dưới một giờ;1-2 giờ;2-5 giờ;Trên 5 giờ",
            "p": "0.3;0.1;0.2;0.4",
            "one_choice": True
        },
        {
            "ques": "5. Điều kiện để ứng dụng CNTT được áp dụng",
            "choice": "Cơ sở vật chất;Sự chủ động của sinh viên;Khả năng tiếp thu của sinh viên;Kỹ năng sử dụng CNTT của giảng viên;Năng lực của giảng viên",
            "p": "0.2;0.2;0.2;0.2;0.2",
            "one_choice": False
        },
        {
            "ques": "6. Ảnh hưởng tiêu cực của các ứng dụng CNTT tới khả năng học tập của bạn.",
            "choice": "Quảng cáo xen ngang làm bạn giảm tập trung;Sử dụng các thiết bị điện tử làm ảnh hưởng tới thị giác và gây mệt mỏi;Sự cám dỗ của mạng xã hội làm bạn sao nhãng trong quá trình học tập;Giảm sự kết nối giữa người với người;Sự phát triển của CNTT khiến bạn phụ thuộc vào chúng",
            "p": "0.2;0.2;0.2;0.2;0.2",
            "one_choice": False
        },
        {
            "ques": '1. Ứng dụng CNTT [Các mạng xã hội ảnh hưởng tích cực đến kết quả học tập của bạn]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0;0.1;0.2;0.3;0.4",
            "one_choice": True
        },
        {
            "ques": '1. Ứng dụng CNTT [Các ứng dụng rất hữu ích cho việc tự học]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0;0.1;0.3;0.2;0.4",
            "one_choice": True
        },
        {
            "ques": '1. Ứng dụng CNTT [Ứng dụng dạy học kết hợp đem lại hiệu quả cao hơn trong học tập]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0;0.1;0.3;0.2;0.4",
            "one_choice": True
        },
        {
            "ques": '1. Ứng dụng CNTT [Đa dạng tài liệu, hỗ trợ quá trình tiếp cận thông tin một cách nhanh chóng và chính thống]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0;0.1;0.3;0.2;0.4",
            "one_choice": True
        },
        {
            "ques": '2. Lợi ích của CNTT [Bạn sử dụng CNTT để tìm và phân tích tài liệu]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0;0;0.1;0.25;0.65",
            "one_choice": True
        },
        {
            "ques": '2. Lợi ích của CNTT [CNTT giúp bạn tiết kiệm thời gian tìm kiếm tài liệu so với phương pháp truyền thống qua sách, báo]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0;0.1;0.2;0.4;0.3",
            "one_choice": True
        },
        {
            "ques": '2. Lợi ích của CNTT [CNTT giúp bạn kết nối được bạn bè và thầy cô để hỗ trợ học tập?]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0.1;0.1;0.2;0.3;0.3",
            "one_choice": True
        },
        {
            "ques": '2. Lợi ích của CNTT [Sử dụng CNTT giúp bạn chủ động tự học một cách linh hoạt]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0.1;0;0.1;0.5;0.3",
            "one_choice": True
        },
        {
            "ques": '2. Lợi ích của CNTT [Phạm vi giáo dục được mở rộng]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0;0.05;0.2;0.4;0.35",
            "one_choice": True
        },
        {
            "ques": '3. Cơ sở vật chất [Chất lượng của phòng học ảnh hưởng tỉ lệ thuận với kết quả học tập của bạn?]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0.1;0.1;0.2;0.25;0.35",
            "one_choice": True
        },
        {
            "ques": '3. Cơ sở vật chất [Phòng thực hành của trường ĐHCNHN đáp ứng được nhu cầu học tập của bạn?]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0.2;0.3;0.2;0.2;0.1",
            "one_choice": True
        },
        {
            "ques": '3. Cơ sở vật chất [Hệ thống wifi ở trường học giúp bạn truy cập Internet dễ dàng và nhanh chóng?]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0.3;0.25;0.25;0.15;0.05",
            "one_choice": True
        },
        {
            "ques": '3. Cơ sở vật chất [Thiết bị cá nhân có vai trò quan trọng trong việc tiếp cận và sử dụng các ứng dụng CNTT?]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0.5;0.3;0.1;0.05;0.05",
            "one_choice": True
        },
        {
            "ques": '4. Ảnh hưởng tới kết quả học tập [Sử dụng CNTT trong ôn tập giúp bạn cải thiện điểm số kiểm tra]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0;0.05;0.15;0.45;0.35",
            "one_choice": True
        },
        {
            "ques": '4. Ảnh hưởng tới kết quả học tập [Sử dụng CNTT giúp bạn có hứng thú hơn trong học tập]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0.05;0;0.1;0.5;0.35",
            "one_choice": True
        },
        {
            "ques": '4. Ảnh hưởng tới kết quả học tập [Kết quả học tập của sinh viên chỉ phụ thuộc vào việc sử dụng CNTT]',
            "choice": "Hoàn toàn không đồng ý;Không đồng ý;Bình thường;Đồng ý;Hoàn toàn đồng ý",
            "p": "0.35;0.25;0.25;0.1;0.05",
            "one_choice": True
        }
    ]
    return map_question_to_answer


def split_choices_str(choices):
    return [i.strip() for i in choices.split(";")]


def split_choices_float(choices):
    return [float(i) for i in choices.split(";")]


def gen_multi_choice_data(num_samples, questions):
    # Tạo dữ liệu giả lập
    fake_data = []

    for _ in range(num_samples):
        responses = {}
        for question, options in questions.items():
            try:
                # Chọn ngẫu nhiên ít nhất 2 lựa chọn cho mỗi câu hỏi
                a = np.array(split_choices_str(options['choice']))
                p = np.array(split_choices_float(options['p']))
                if options['one_choice']:
                    num_choices = 1
                    selected_options = np.random.choice(
                        a=a,
                        size=num_choices,
                        p=p,
                        replace=False
                    )

                else:
                    num_choices = np.random.randint(1, len(a))
                    selected_options = np.random.choice(
                        a=a,
                        size=num_choices,
                        p=p,
                        replace=False
                    )
                responses[question] = selected_options
            except Exception as e:
                print(f"Error at question: {question} - {e}")
        fake_data.append(responses)
        st.warning(f"Error: {e}")

    # Kiểm tra phân phối của các lựa chọn đã chọn
    for question, options in questions.items():
        selected_counts = []
        for response in fake_data:
            if question in response:
                selected_counts.append(len(response[question]))
                
    return fake_data


def convert_list_to_str(df):
    for col in df.columns:
        df[col] = df[col].apply(lambda x: ",".join(x))
    return df


def app():
    data = init_db()
    st.header("Ứng dụng tạo dữ liệu giả lập")
    
    # Show the editable table
    st.info("Cột choice, p: Các đáp án và xác suất cách nhau bởi dấu ; (chấm phẩy) và không có dấu cách - Số thập phân phân cách bởi dấu chấm (VD: 0.25)")
    st.info("Phải điền đủ các giá trị xác suất tương ứng với từng đáp án kể cả xác suất 0 (VD: Câu có 5 đáp án thì cột p cũng phải có 5 xác suất)")
    st.info("Lưu ý: Tổng xác suất p của một câu hỏi phải bằng 1")
    st.info("Cột one_choice: Tích chọn nếu câu hỏi chỉ được chọn một lựa chọn, bỏ chọn nếu được chọn nhiều lựa chọn")
    st.info("Nếu muốn khôi phục lại thiết lập câu hỏi gốc ban đầu -> Tải lại trang (F5)")
    st.write("Thiết lập dữ liệu giả lập vào bảo dưới đây!!!")
    data = st.data_editor(
        pd.DataFrame(data),
        num_rows="dynamic",
        disabled=False
    ).set_index("ques").transpose()
    samples = st.slider("Số lượng mẫu dữ liệu", 1, 1000, 100)
    
    fake_data = None
    
    # Show button to generate data
    if st.button("Tạo dữ liệu"):
        fake_data = pd.DataFrame(gen_multi_choice_data(num_samples=samples, questions=data.to_dict()))
        refeactor_fake_data = convert_list_to_str(fake_data.copy())
        st.write(fake_data)

        st.download_button(
            label="Tải dữ liệu",
            data=pd.DataFrame(refeactor_fake_data).to_csv(index=False),
            file_name="fake_data.csv",
            mime="text/csv"
        )
        

if __name__ == '__main__':
    app()