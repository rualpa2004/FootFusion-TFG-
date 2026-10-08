import { Eye, EyeOff, Lock } from "lucide-react";
import { useState, type InputHTMLAttributes } from "react";
import { TextInput } from "./TextInput";

interface PasswordInputProps extends Omit<InputHTMLAttributes<HTMLInputElement>, 'type'> {
    hasError?: boolean;
}

export function PasswordInput(props: PasswordInputProps) {
    // useState is justified here: whether the password is visible is ephemeral UI state that
    // lives only in this component. It is not data loaded from anywhere (so a loader does not
    // apply) and it is not sent anywhere (so an action does not apply). Toggling it must
    // re-render the input with type="text" or type="password", which requires React state.
    const [isVisible, setIsVisible] = useState(false);

    return (
        <TextInput
            {...props}
            icon={Lock}
            type={isVisible ? 'text' : 'password'}
            trailing={
                <button
                    type="button"
                    onClick={() => setIsVisible((visible) => !visible)}
                    aria-label={isVisible ? 'Ocultar contraseña' : 'Mostrar contraseña'}
                    className="shrink-0 text-muted transition-colors hover:text-white"
                >
                    {isVisible
                        ? <EyeOff className="size-[18px]" aria-hidden/>
                        : <Eye className="size-[18px]" aria-hidden/>}
                </button>
            }
        />
    );
}
